#pragma once

#include "PlotJuggler/messageparser_base.h"

#include <google/protobuf/descriptor.h>
#include <google/protobuf/reflection.h>
#include <google/protobuf/dynamic_message.h>
#include <google/protobuf/io/zero_copy_stream_impl.h>
#include <google/protobuf/io/tokenizer.h>
#include <google/protobuf/compiler/parser.h>
#include <google/protobuf/compiler/importer.h>

#include <QCheckBox>
#include <QDebug>
#include <string>

#include "ui_protobuf_parser.h"

using namespace PJ;

class ProtoErrorCollector: public google::protobuf::compiler::MultiFileErrorCollector
{
public:
  void AddError(const std::string& filename, int line, int, const std::string& message) override;

  void AddWarning(const std::string& filename, int line, int, const std::string& message) override;

  void showErrors();
private:
  QString _error_msg;
};

class ProtobufParser : public MessageParser
{
public:
  ProtobufParser(const std::string& topic_name, PlotDataMapRef& data,
                 const google::protobuf::Descriptor* descriptor)
    : MessageParser(topic_name, data)
    , _msg_descriptor(descriptor)
  {
  }

  bool parseMessage(const MessageRef serialized_msg, double& timestamp) override;

protected:

  google::protobuf::DynamicMessageFactory _msg_factory;
  const google::protobuf::Descriptor* _msg_descriptor;
};

//------------------------------------------

class ProtobufParserCreator : public MessageParserCreator
{
  Q_OBJECT
  Q_PLUGIN_METADATA(IID "facontidavide.PlotJuggler3.MessageParserCreator")
  Q_INTERFACES(PJ::MessageParserCreator)

  void loadSettings();

  void saveSettings();

  void importFile(QString filename);

public:
  ProtobufParserCreator();

  ~ProtobufParserCreator() override;

  const char* name() const override
  {
    return "ProtobufParser";
  }

  MessageParserPtr createInstance(const std::string& topic_name,
                                  PlotDataMapRef& data) override;

  QWidget* optionsWidget() override
  {
    return _widget;
  }

protected:

  Ui::ProtobufLoader* ui;
  QWidget* _widget;

  google::protobuf::compiler::DiskSourceTree _source_tree;
  ProtoErrorCollector _error_collector;
  std::unique_ptr<google::protobuf::compiler::Importer> _importer;

  struct Info
  {
    QString file_path;
    QByteArray proto_text;
    const google::protobuf::FileDescriptor* file_descriptor = nullptr;
    std::map<QString,const google::protobuf::Descriptor*> descriptors;
  };
  Info _loaded_file;

  const google::protobuf::Descriptor* _selected_descriptor = nullptr;

  bool updateUI();

private slots:

  void onIncludeDirectory();

  void onLoadFile();

  void onRemoveInclude();

  void onComboChanged(const QString &text);
};



